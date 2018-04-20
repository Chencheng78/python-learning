import itertools
import mimetools
import mimetypes
import urllib2
import os
import hashlib


class MultiPartForm(object):
    """Accumulate the data to be used when posting a form."""

    def __init__(self):
        self.form_fields = []
        self.files = []
        self.boundary = mimetools.choose_boundary()
        return

    def get_content_type(self):
        return 'multipart/form-data; boundary=%s' % self.boundary

    def add_field(self, name, value):
        """Add a simple field to the form data."""
        self.form_fields.append((name, value))
        return

    def add_file(self, fieldname, filename, fileHandle, mimetype=None):
        """Add a file to be uploaded."""
        body = fileHandle.read()
        if mimetype is None:
            mimetype = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
        self.files.append((fieldname, filename, mimetype, body))
        return

    def __str__(self):
        """Return a string representing the form data, including attached files."""
        # Build a list of lists, each containing "lines" of the
        # request.  Each part is separated by a boundary string.
        # Once the list is built, return a string where each
        # line is separated by '\r\n'.
        parts = []
        part_boundary = '--' + self.boundary

        # Add the form fields
        parts.extend(
            [part_boundary,
             'Content-Disposition: form-data; name="%s"' % name,
             '',
             value,
             ]
            for name, value in self.form_fields
        )

        # Add the files to upload
        parts.extend(
            [part_boundary,
             'Content-Disposition: form-data; name="%s"; filename="%s"' % \
             (field_name, filename),
             'Content-Type: %s' % content_type,
             '',
             body,
             ]
            for field_name, filename, content_type, body in self.files
        )

        # Flatten the list and add closing boundary marker,
        # then return CR+LF separated data
        flattened = list(itertools.chain(*parts))
        flattened.append('--' + self.boundary + '--')
        flattened.append('')
        return '\r\n'.join(flattened)

'''
Calculate file size and Hash.
'''


def file_size(filename):
    size = os.stat(filename)
    return int(size.st_size)


def file_hash(filename):
    opened_file = open(filename, 'rb')
    sha256 = hashlib.sha256(opened_file.read())
    return sha256.hexdigest()


if __name__ == '__main__':
    # Create the form with simple fields
    form = MultiPartForm()

    # form-data field builder
    print file_size('config.py')
    print file_hash('config.py')
    form.add_file('config.py', '{"size":33,"sha256":"08ab04722e0ac71ce04b40aea20e4ab5b52d9ce860718c7a0bfed424ca27702c"}',
                  fileHandle=open('config.py', 'rb'))

    # Build the request
    request = urllib2.Request('http://10.5.51.68:3000/drives/86fd9ffc-9ab0-4bf9-abe4-b35f0a07881c/dirs/86fd9ffc-9ab0-4bf9-abe4-b35f0a07881c/entries')

    request.add_header('Authorization', 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1dWlkIjoiNjU2Yzk3YmQtMjIzYy00OTg2LThlN2UtMTE3YTMxMTNlNTg2In0.sya0s8oWrHTaW12_zWBbkigYpLU2VrIbkOF2po4Yq-A')
    body = str(form)
    request.add_header('Content-type', form.get_content_type())
    request.add_header('Content-length', len(body))
    request.add_data(body)

    print 'OUTGOING DATA:'
    print request.get_data()

    print 'SERVER RESPONSE:'
    print urllib2.urlopen(request).read()
