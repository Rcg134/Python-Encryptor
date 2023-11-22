import argparse
import PyPDF2

class PdfEncryptor:
    def __init__(self, input_path, output_path, password):
        self.input_path = input_path
        self.output_path = output_path
        self.password = password

    def encrypt_pdf(self):
        with open(self.input_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            pdf_writer = PyPDF2.PdfFileWriter()

            for page_num in range(pdf_reader.numPages):
                pdf_writer.addPage(pdf_reader.getPage(page_num))

            pdf_writer.encrypt(self.password)

            with open(self.output_path, 'wb') as output_file:
                pdf_writer.write(output_file)
        print('Done Enryption')

    def decrypt_pdf(self, decrypted_output_path):
        with open(self.output_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            pdf_reader.decrypt(self.password)

            pdf_writer = PyPDF2.PdfFileWriter()

            for page_num in range(pdf_reader.numPages):
                pdf_writer.addPage(pdf_reader.getPage(page_num))

            with open(decrypted_output_path, 'wb') as output_file:
                pdf_writer.write(output_file)
        print('Done Decryption')

def main():
    parser = argparse.ArgumentParser(description='Encrypt and decrypt PDF files.')
    parser.add_argument('-i', '--input', help='Input PDF file path', required=True)
    parser.add_argument('-o', '--output', help='Output PDF file path', required=True)
    parser.add_argument('-p', '--password', help='Password for encryption/decryption', required=True)

    args = parser.parse_args()
    encryptor = PdfEncryptor(args.input, args.output, args.password)
    encryptor.encrypt_pdf()
    encryptor.decrypt_pdf('decrypted.pdf')

# Call main function eweqwqe
main()
