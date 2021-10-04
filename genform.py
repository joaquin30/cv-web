def genform(file):
    ans ='<form action="/cv" method="POST">\n'
    with open(file, 'r') as f:
        for s in f:
            s = s.strip()
            ans += f'<label for="{s}" class="form-label">{s.capitalize()}</label><br>\n<input type="text" id="{s}" name="{s}" class="form-input"><br>\n'
    return ans + '<br><input type="submit" class="form-button"><input type="reset" class="form-button">\n</form>'

if __name__ == '__main__':
    print(genform('form.txt'))