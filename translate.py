from googletrans import Translator

def translate_file(input_path, output_path):
    # Read the input file
    with open(input_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Initialize the translator
    translator = Translator(service_urls=['translate.google.com'])

    # Translate the text
    translated_text = translator.translate(text, src='ms', dest='en').text

    # Save the translated text to the output file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(translated_text)

# Specify the paths of the input and output files
input = 'C:/Users/User/Documents/Study/Degree/Year 3/Sem 1/Natural Language Processing/project/output/47.txt'
output = 'C:/Users/User/Documents/Study/Degree/Year 3/Sem 1/Natural Language Processing/project/translated/47.txt'

# Translate the input file and save the result
translate_file(input, output)
