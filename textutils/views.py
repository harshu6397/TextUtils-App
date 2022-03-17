# I have create this file --> Harsh Kumar
from django.shortcuts import render
import string

def index(request):
    return render(request, 'index.html', {'error' : ' '})

def analyze(request):

    # Get the value
    value = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    remove_newline = request.POST.get('remove_newline', 'off')
    remove_space = request.POST.get('remove_space', 'off')
    char_counter = request.POST.get('char_counter', 'off')

    # list for purposes
    lst_purpose = []
     
    # logic for remove punctuation
    if removepunc == 'on':
        analyze_text = ''
        for char in value:
            if char not in string.punctuation:
                analyze_text = analyze_text + char
        lst_purpose.append('Remove punctuation')
        value = analyze_text

    # logic for converting in Uppercase
    if uppercase == 'on':
        analyze_text = value.upper()
        lst_purpose.append('Change to Uppercase')
        value = analyze_text
    
    # logic for converting in Lowercase
    if lowercase == 'on':
        analyze_text = value.lower()
        lst_purpose.append('Change to Lowercase')
        value = analyze_text

    # Logic for removing newlines
    if remove_newline == 'on':
        analyze_text = ''
        for char in value:
            if char != '\n' and char != '\r':
                analyze_text = analyze_text + char
        lst_purpose.append('Remove Newlines')
        value = analyze_text

    # Logic for removing extra spaces
    if remove_space == 'on':
        analyze_text = ''
        for index, char in enumerate(value):
            if not(value[index] == " " and value[index+1]==" "):
               analyze_text =analyze_text + char
        lst_purpose.append('Remove Extra Spaces')
        value = analyze_text
    
    # Parameters to pass in template
    params = {
            'purpose' : 'The purpose is: ' + ', '.join(lst_purpose),
            'analyze_text' : value,
    }

    # code for showing error if no functionality is selected
    if removepunc == 'off' and char_counter == 'off' and remove_newline == 'off' and remove_space == 'off' and uppercase == 'off' and lowercase == 'off':
        return render(request, 'index.html', {'value' : value, 'error' : 'ERROR: Please check one of the functionalities!!'})

    # logic to return no of characters and render the templates
    if char_counter == 'on':
        lst_purpose.append('Count the number of charcaters')
        params = {
            'purpose' : 'The purpose is: ' + ', '.join(lst_purpose),
            'analyze_text' : value + '\n' + "The number of character is: " + str(len(value)),
        }   
        return render(request, 'analyze.html', params)
    else:
        return render(request, 'analyze.html', params)
