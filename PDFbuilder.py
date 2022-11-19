import tkinter as tk
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox
import os
import webbrowser as wb
import pdfkit
namaSaya = ''
f = open('wkhtmltopdf/lib/themes.pbfl','r')
temaAnda = f.read()
f.close()
f = open('wkhtmltopdf/lib/nFont.pbfl','r')
nFont = f.read()
f.close()
f = open('wkhtmltopdf/dimFont.pbfl','r')
dimFont = int(f.read())
f.close()
class Menubar:
    def __init__(self, parent):
        font_specs = (nFont, dimFont-5)
        if temaAnda == 'claro':
            coB = 'white'
            coF = 'black'
        else:
            coB = 'black'
            coF = 'green'  
        menubar = tk.Menu(parent.master, font=font_specs)
        parent.master.config(menu=menubar)
        file_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0,fg=coF,bg=coB)
        file_dropdown.add_command(label="\U0001F4DD New File",
                                  accelerator="Ctrl+N",
                                  command=parent.new_file)
        file_dropdown.add_command(label="░ Open File",
                                  accelerator="Ctrl+O",
                                  command=parent.open_file)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="↓ Save File",
                                  accelerator="Ctrl+S",
                                  command=parent.save_file)
        file_dropdown.add_command(label="▼ Save as",
                                  accelerator="Ctrl+Shift+S",
                                  command=parent.save_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="\U00002622 Exit",
                                  accelerator="Alt+F4",
                                  command=parent.master.destroy)
        file_dropdown.add_command(label="⟳Reload",
                                  accelerator="Alt+F5",
                                  command=parent.ricarica)
        edit_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0,fg=coF,bg=coB)
        edit_dropdown.add_command(label="\U00002936 Undo",
                                   accelerator="Ctrl+Z",
                                     command=parent.indietro)
        edit_dropdown.add_command(label="\U00002937 Redo",
                                   accelerator="Ctrl+Y",
                                     command=parent.avanti)
        edit_dropdown.add_separator()
        edit_dropdown.add_command(label="\U00002702 Cut",
                                   accelerator="Ctrl+X",
                                     command=parent.taglia)
        edit_dropdown.add_command(label="🐒 Copy",
                                  accelerator="Ctrl+C",
                                     command=parent.copia)
        edit_dropdown.add_command(label="\U0001F35D Paste",
                                  accelerator="Ctrl+V",
                                     command=parent.incolla)
        edit_dropdown.add_command(label="\U0001F4E6 Select All",
                                  accelerator="Ctrl+A",
                                     command=parent.selezionaTutto)
        edit_dropdown.add_separator()
        edit_dropdown.add_command(label="\U0001F50E Find",
                                  accelerator="Ctrl+F",
                                     command=parent.finder)
        edit_dropdown.add_command(label="\U0000FFFD Replace",
                                     accelerator="Ctrl+H",
                                     command=parent.sostituisci)
        edit_dropdown.add_separator()
        edit_dropdown.add_command(label=" 🖨️ Print",
                                  accelerator="Ctrl+J",
                                     command=parent.stampa)
        format_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0,fg=coF,bg=coB)
        format_dropdown.add_command(label="\U0001F670 Change Font",
                                    accelerator="Ctrl+Shift+F",
                                     command=parent.cambiaFont)
        format_dropdown.add_command(label="± Change Font Size",
                                    accelerator="Ctrl+I",
                                     command=parent.cambiaDimensione)
        format_dropdown.add_separator()
        format_dropdown.add_command(label="\U0001F3A8 Change Background Color",
                                    accelerator="Ctrl+Shift+C",
                                     command=parent.cambiaColore)
        format_dropdown.add_command(label="\U0001F3A8 Change Characters Color",
                                    accelerator="Ctrl+Shift+g",
                                     command=parent.cambiaColoreFG)
        format_dropdown.add_command(label="▓ Change Theme",
                                    accelerator="Ctrl+T",
                                     command=parent.cambiaTema)
        format_dropdown.add_separator()
        format_dropdown.add_command(label="\U0001F4A5 Clear Screen",
                                    accelerator="Ctrl+R",
                                     command=parent.pulisciSchermo)
        convert_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0,fg=coF,bg=coB)
        convert_dropdown.add_command(label="\U0001F4D5 Build as PDF",
                                  accelerator="F5",
                                  command=parent.build)
        convert_dropdown.add_command(label="\U00002705 Check Text",
                                  accelerator="F3",
                                  command=parent.CheckASCII)
        convert_dropdown.add_command(label="\U0000274C Go to nonASCII.html",
                                  accelerator="F2",
                                  command=parent.nonASCIIcheck)
        about_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0,fg=coF,bg=coB)
        about_dropdown.add_command(label="♠ About",
                                   accelerator="Ctrl+Shift+A",
                                     command=self.show_about_message)
        about_dropdown.add_command(label="♣ Version",
                                   accelerator="Ctrl+Shift+V",
                                     command=self.show_release_notes)
        about_dropdown.add_command(label="❤ What's new?",
                                   accelerator="Ctrl+Shift+N",
                                     command=self.show_new_notes)
        help_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0,fg=coF,bg=coB)
        help_dropdown.add_command(label="¿ Help Guide",
                                  accelerator="Ctrl+Shift+H",
                                     command=self.helper)
        help_dropdown.add_command(label="∞ Documentation (Only English)",
                                  accelerator="Ctrl+D",
                                     command=parent.documents)
        help_dropdown.add_separator()
        help_dropdown.add_command(label="© Templates",
                                  accelerator="Ctrl+Shift+T",
                                     command=parent.templates)
        menubar.add_cascade(label="File", menu=file_dropdown)
        menubar.add_cascade(label="Edit", menu=edit_dropdown)
        menubar.add_cascade(label="Format", menu=format_dropdown)
        menubar.add_cascade(label="Convert", menu=convert_dropdown)
        menubar.add_cascade(label="About", menu=about_dropdown)
        menubar.add_cascade(label="Help", menu=help_dropdown)
    def helper(self):
        wb.open("http://masteradon.altervista.org/LP/HowToUsePDFbuilder.pdf", new=0, autoraise=True)
    def show_about_message(self):
        box_title = "About PDF-Builder",
        box_message = "PDF-Builder allow you to create your PDF file without use any converter. Write here the file you want and click build to create the pdf file. You'll get output in same directory where you choose to save the file. You can't edit pdf with this, you can edit your pdf using code .pbf and building pdf again. For more information click Help"
        messagebox.showinfo(box_title, box_message)  
    def show_release_notes(self):
        box_title = "Release Notes",
        box_message = "Version 2.0 - PDF-Builder"
        messagebox.showinfo(box_title, box_message)
    def show_new_notes(self):
        box_title = "What's New?",
        box_message = "Better tab space, More Buttons, Better Colors, New Theme, New Functions!\nIn the next update will be add: Personalized Theme, More Templates, an easier way to change colors and theme, pbf templates (not only html like now), more Buttons to avoid write code and make it more user friendly and all languages translation!"
        messagebox.showinfo(box_title, box_message)
class Statusbar:
    def __init__(self, parent):
        font_specs = (nFont, dimFont-5)
        if temaAnda == 'claro':
            coB = 'white'
            coF = 'black'
        else:
            coB = 'black'
            coF = 'green'
        self.status = tk.StringVar()
        self.status.set("PDF-Builder - ver-2.0")
        label = tk.Label(parent.textarea, textvariable = self.status, fg="black",
                         bg="white", anchor='sw', font=font_specs)
        label.pack(side=tk.BOTTOM, fill=tk.BOTH)
    def update_status(self, value, *args):
        print(value)
        if isinstance(value, bool):
            self.status.set("The File has been saved!")
        else:
            print(value)
            self.status.set("PDF-Builder - ver-2.0 \t\t Characters: "+str(len(value))+"\t Words: "+str(len(value.split(' '))))
    def updateB_status(self, *args):
        f = open('wkhtmltopdf/bn.txt','r')
        cont = int(f.read())
        f.close()
        f = open('wkhtmltopdf/bn.txt','w')
        f.write(str(cont+1))
        f.close()
        if isinstance(args[0], bool):
            self.status.set("The File has been converted into a PDF!")
        else:
            self.status.set("PDF-Builder - ver-2.0")    
class PyText:
    def __init__(self, master):
        master.title(" - Untitled - PDF-Builder")
        master.geometry("800x600+200+200")
        font_specs = (nFont, dimFont)
        if temaAnda == 'claro':
            coB = 'white'
            coF = 'black'
            cb='black'
        else:
            coB = 'black'
            coF = 'green'
            cb='green'
        self.master = master
        self.filename = None
        self.textarea=tk.Text(master, font=font_specs,fg=coF,bg=coB,undo=True,insertbackground=cb)
        self.scroll=tk.Scrollbar(master, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.menubar = Menubar(self)
        self.textarea.config(tabs = ("22"))
        self.statusbar = Statusbar(self)
        self.bind_shortcuts()
    def set_window_title(self, name=None):
        global namaSaya
        if name:
            namaSaya = name
            self.master.title(name + "- ")
        else:
            self.master.title(" - Untitled - ")
    def pulisciSchermo(self,*args):
        f = open('wkhtmltopdf/bn.txt','w')
        f.write('0')
        f.close()
        self.textarea.delete(1.0, tk.END)
    def selezionaTutto(self,*args):
        self.textarea.tag_add('sel', 1.0, tk.END)
    def cambiaTema(self,*args):
        if temaAnda == 'claro':
            f = open('wkhtmltopdf/lib/themes.pbfl','w')
            f.write('010101010101010')
            f.close()
            box_title = "Dark Theme Ready!",
            box_message = "Restart the application to load dark theme"
            messagebox.showinfo(box_title, box_message)
        else:
            f = open('wkhtmltopdf/lib/themes.pbfl','w')
            f.write('claro')
            f.close()
            box_title = "White Theme Ready!",
            box_message = "Restart the application to load white theme"
            messagebox.showinfo(box_title, box_message)
    def taglia(self,*args):
        if self.textarea.selection_get():
            selected = self.textarea.selection_get()
            self.textarea.delete("sel.first", "sel.last")
            master.clipboard_clear()
            master.clipboard_append(selected)
    def copia(self,*args):
        if self.textarea.selection_get():
            selected = self.textarea.selection_get()
            master.clipboard_clear()
            master.clipboard_append(selected)     
    def incolla(self,*args):
        position = self.textarea.index(tk.INSERT)
        self.textarea.insert(position,)
    def cambiaColoreFG(self,*args):
        my_color = colorchooser.askcolor()[1]
        if my_color:
            self.textarea.config(fg=my_color)
    def cambiaColore(self,*args):
        my_color = colorchooser.askcolor()[1]
        if my_color:
            self.textarea.config(bg=my_color)
    def stampa(self,*args):
        file_to_print = filedialog.askopenfilename(initialdir="C:/gui/", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
        if file_to_print:
            win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)
    def cambiaFont(self,*args):
        top= tk.Toplevel(master)
        top.iconbitmap('image/radioactive.ico')
        top.title('Change Font')
        top.geometry("250x170")
        lab1 = tk.Label(top,text='Choose New Font \nclick Apply and reload PDF-Builder\n to Apply changes').pack(pady=5)
        options = [
            'Arial',
            'Algerian',
            'Helvetica',
            'Times',
            'Batang',
            'BatangChe',
            'DFKai-SB',
            'Gunsuh',
            'MS Gothic',
            'Calibri',
            ]
        clicked = tk.StringVar()
        clicked.set(nFont)
        menus = tk.OptionMenu(top, clicked, *options)
        menus.pack()
        def doIT():
            f = open('wkhtmltopdf/lib/nFont.pbfl','w')
            f.write(clicked.get())
            print(clicked.get())
            f.close()
            lab = tk.Label(top,text='Font Modified! ').pack(pady=5)
            top.destroy()
        tk.Button(top,text= "Apply", command= lambda:doIT()).pack(pady= 5)
        button= tk.Button(top, text="Close", command=lambda:top.destroy())
        button.pack(pady=5)
    def documents(self,*args):
        wb.open("http://masteradon.altervista.org/LP/HTUPDF/Documentation.pdf", new=0, autoraise=True)
    def cambiaDimensione(self,*args):
        top= tk.Toplevel(master)
        top.iconbitmap('image/radioactive.ico')
        top.title('Change Font Dimension')
        top.geometry("250x150")
        lab1 = tk.Label(top,text='insert your new font dimension (number), \nclick Apply and reload PDF-Builder\n to Apply changes').pack(pady=5)
        entry1= tk.Entry(top, width= 25)
        entry1.pack()
        def doIT():
            d = entry1.get()
            try:
                app = int(d)
                f = open('wkhtmltopdf/dimFont.pbfl','w')
                f.write(d)
                f.close()
                lab = tk.Label(top,text='Font Dimension Modified! ').pack(pady=5)
            except Exception as e:
                print(e)
                box_title = "Impossible Change Font Dimension",
                box_message = "You need insert an integer"
                messagebox.showerror(box_title, box_message)
        tk.Button(top,text= "Apply", command= lambda:doIT()).pack(pady= 5)
        button= tk.Button(top, text="Close", command=lambda:top.destroy())
        button.pack(pady=5)
    def ricarica(self,*args):
        os.system('start PDFbuilder.exe')
        exit()
    def templates(self,*args):
        top= tk.Toplevel(master)
        top.iconbitmap('image/radioactive.ico')
        top.title('Templates')
        top.geometry("250x150")
        lab1 = tk.Label(top,text='Choose the template to load the \nHTML code and the PDF view').pack(pady=5)
        options = [
            'Report',
            'Document',
            'Table'
            ]
        clicked = tk.StringVar()
        clicked.set('Select Template')
        menus = tk.OptionMenu(top, clicked, *options)
        menus.pack()
        def doIT():
            print(clicked.get())
            self.textarea.delete(1.0, tk.END)
            if clicked.get() == 'Report':
                f = open('wkhtmltopdf/templates/relation.pbfl', 'r')
                self.textarea.insert(1.0, f.read())
                self.set_window_title('Report Template')
                os.system('start wkhtmltopdf/templates/Report.pdf')
                f.close()
                top.destroy()
            if clicked.get() == 'Document':
                f = open('wkhtmltopdf/templates/document.pbfl', 'r')
                self.textarea.insert(1.0, f.read())
                self.set_window_title('Document Template')
                os.system('start wkhtmltopdf/templates/Document.pdf')
                f.close()
                top.destroy()
            if clicked.get() == 'Table':
                f = open('wkhtmltopdf/templates/table.pbfl', "r")
                self.textarea.insert(1.0, f.read())
                self.set_window_title('Table Template')
                os.system('start wkhtmltopdf/templates/table.pdf')
                f.close()
                top.destroy()
        tk.Button(top,text= "Apply", command= lambda:doIT()).pack(pady= 5)
        button= tk.Button(top, text="Close", command=lambda:top.destroy())
        button.pack(pady=5)
    def cambiaLingua(self,*args):
        pass
    def indietro(self,*args):
        pass
    def avanti(self,*args):
        pass
    def CheckASCII(self,*args):
        testo = self.textarea.get(1.0,tk.END)
        wordsAllowed = ['è','é','°','à','#','ù','ò','$','@','&','%','€','"',
                        "'",'!','?','(',')','/','|','=','£','^','ì','+','-',
                        '*','_']
        for word in wordsAllowed:
            testo = testo.replace(word,'A')
        for word in testo:
            if not word.isascii():
                self.textarea.tag_remove('found', 1.0, tk.END)
                ser = word
                if ser:
                    idx = '1.0'
                    while 1:
                        idx = self.textarea.search(ser, idx, nocase=1,
                                        stopindex=tk.END)
                        if not idx: break
                        lastidx = '%s+%dc' % (idx, len(ser))           
                        self.textarea.tag_add('found', idx, lastidx)
                        idx = lastidx
                    self.textarea.tag_config('found', foreground='white', background='red')                
        if testo.isascii():
            box_title = "Text Approved",
            box_message = "Your Text is buildable as PDF"
            messagebox.showinfo(box_title, box_message)
        else:
            box_title = "Text Not Approved",
            box_message = "Your Text is not buildable as PDF! Words not allowed are marked in red"
            messagebox.showerror(box_title, box_message)
    def new_file(self, *args):
        f = open('wkhtmltopdf/bn.txt','w')
        f.write('0')
        f.close()
        self.textarea.delete(1.0, tk.END)
        self.filename = None
        self.set_window_title()
    def open_file(self, *args):
        self.filename = filedialog.askopenfilename(
            defaultextension = "*.*",
            filetypes=[("All Files", "*.*"),
                       ("PDF-Builder", "*.pbf"),])
        if self.filename:
            self.textarea.delete(1.0, tk.END)
            f = open(self.filename, "r")
            lif = open('wkhtmltopdf/bn.txt','w')
            lif.write(str(len(f.read())-1))
            f.close()
            f = open(self.filename, "r")
            self.textarea.insert(1.0, f.read())
            self.set_window_title(self.filename)
            lif.close()
            f.close()
    def save_file(self, *args):
        testo = self.textarea.get(1.0,tk.END)
        wordsAllowed = ['è','é','°','à','#','ù','ò','$','@','&','%','€','"',
                        "'",'!','?','(',')','/','|','=','£','^','ì','+','-',
                        '*','_']
        for word in wordsAllowed:
            testo = testo.replace(word,'Allowed')
        if testo.isascii():
            if self.filename:
                try:
                    textarea_content = self.textarea.get(1.0, tk.END)
                    with open(self.filename, "w") as f:
                        f.write(textarea_content)
                    self.statusbar.update_status(True)
                except Exception as e:
                    print(e)
            else:
                self.save_as()
        else:
            box_title = "ERROR: Cannot convert non-ASCII characters",
            box_message = "Not-ASCII characters detected. Go at http://masteradon.altervista.org/LP/nonASCII.html to detect which is the unconvertible characters!"
            messagebox.showerror(box_title, box_message)  
    def build(self, *args):
        if namaSaya[-4:]=='.pbf':
            if not self.filename:
                self.save_file()
            try:
                pat = namaSaya+'.html'
                fal = open(pat,'w')
                testo = self.textarea.get(1.0,tk.END)
                testo = testo.replace('<image=','<img src=')
                testo = testo.replace('<bold>','<b>')
                testo = testo.replace('</bold>','</b>')
                testo = testo.replace('<mainTitle>','<h1>')
                testo = testo.replace('</mainTitle>','</h1>')
                testo = testo.replace('<subTitle>','<h2>')
                testo = testo.replace('</subTitle>','</h2>')
                testo = testo.replace('<textLine>','<p>')
                testo = testo.replace('</textLine>','</p>')
                testo = testo.replace('<color=','<font color=')
                testo = testo.replace('</color>','</font>')
                testo = testo.replace('<row>','<tr>')
                testo = testo.replace('</row>','</tr>')
                testo = testo.replace('<column>','<td>')
                testo = testo.replace('</column>','</td>')
                testo = testo.replace('<link=','<a href=')
                testo = testo.replace('</link>','</a>')
                testo = testo.replace('<EndLine>','<br>')
                fal.write(testo)
                fal.close()
            except Exception as e:
                print(e)
            funo = open(namaSaya+'.html','r')
            riga = funo.read()
            funo.close()
            print(riga)
            if '<br><br><br><h5><i>Created with <a href="http://masteradon.altervista.org/EN/casual/programs.html#PBF">PDF-Builder</a></i></h5>' in riga:       
                config = pdfkit.configuration(wkhtmltopdf = 'wkhtmltopdf/bin/wkhtmltopdf.exe')
                pdfkit.from_file(namaSaya+'.html',namaSaya[:len(namaSaya)-4]+'.pdf',configuration=config,options={'enable-local-file-access': None})
                os.remove(namaSaya+'.html')
            else:
                f = open(namaSaya+'.html','a')
                f.write('<br><br><br><h5><i>Created with <a href="http://masteradon.altervista.org/EN/casual/programs.html#PBF">PDF-Builder</a></i></h5>')
                f.close()
                config = pdfkit.configuration(wkhtmltopdf = 'wkhtmltopdf/bin/wkhtmltopdf.exe')
                pdfkit.from_file(namaSaya+'.html',namaSaya[:len(namaSaya)-4]+'.pdf',configuration=config,options={'enable-local-file-access': None})
                os.remove(namaSaya+'.html')
            self.statusbar.updateB_status(True)
            try:
                os.system(namaSaya[:len(namaSaya)-4]+'.pdf')
            except Exception as e:
                pass
        else:
            box_title = "ERROR",
            box_message = "Can't convert a not-pbf file!"
            messagebox.showerror(box_title, box_message)  
    def chiudi(self, *args):
        try:
            f = open('wkhtmltopdf/bn.txt','w')
            f.write('0')
            f.close()
            exit()
        except Exception as e:
            print("ERROR: ",end='')
            print(e)
    def save_as(self, *args):
        testo = self.textarea.get(1.0,tk.END)
        wordsAllowed = ['è','é','°','à','#','ù','ò','$','@','&','%','€','"',
                        "'",'!','?','(',')','/','|','=','£','^','ì','+','-',
                        '*','_']
        for word in wordsAllowed:
            testo = testo.replace(word,'Allowed')
        if testo.isascii():
            try:
                new_file = filedialog.asksaveasfilename(
                    initialfile = "Untitled.pbf",
                    defaultextension = "*.*",
                    filetypes=[("PDF-Builder", "*.pbf"),
                               ("All Files", "*.*"),])
                textarea_content = self.textarea.get(1.0, tk.END)
                with open(new_file, "w") as f:
                    f.write(textarea_content)
                self.filename = new_file
                self.set_window_title(self.filename)
                self.statusbar.update_status(True)
            except Exception as e:
                print("ERROR: ",end='')
                print(e)
        else:
            box_title = "ERROR: Cannot convert non-ASCII characters",
            box_message = "Not-ASCII characters detected. Go at http://masteradon.altervista.org/LP/nonASCII.html to detect which is the unconvertible characters!"
            messagebox.showerror(box_title, box_message) 
    def nonASCIIcheck(self,*args):
        wb.open("http://masteradon.altervista.org/LP/nonASCII.html?txt="+self.textarea.get(1.0,tk.END), new=0, autoraise=True)
    def cerca(self,*args):
        self.textarea.tag_remove('found', 1.0, tk.END)
        ser = self.entry.get()
        if ser:
            idx = '1.0'
            while 1:
                idx = self.textarea.search(ser, idx, nocase=1,
                                stopindex=tk.END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(ser))
                
                self.textarea.tag_add('found', idx, lastidx)
                idx = lastidx
            self.textarea.tag_config('found', foreground='white', background='blue')
        self.entry.focus_set()
    def finder(self,*args):
        if temaAnda == 'claro':
            coB = 'white'
            coF = 'black'
        else:
            coB = 'black'
            coF = 'green'
        top= tk.Toplevel(master)
        top.iconbitmap('image/radioactive.ico')
        top.title('Finder')
        top.geometry("250x100")
        global entry
        self.entry = tk.Entry(top, width= 25)
        self.entry.pack()
        def distruggi():
            self.textarea.tag_config('found', foreground=coF,background=coB)
            top.destroy()
        tk.Button(top,text= "Find", command=self.cerca).pack(pady= 5)
        button= tk.Button(top, text="Close", command=distruggi)
        button.pack(pady=5)
    def do_popup(self,event):
        font_specs = (nFont, dimFont-5)
        if temaAnda == 'claro':
            coB = 'white'
            coF = 'black'
        else:
            coB = 'black'
            coF = 'green'
        menuclick = tk.Menu(master, font=font_specs, tearoff=0)
        menuclick.add_command(label="Cut",command=self.taglia)
        menuclick.add_command(label="Copy",command=self.copia)
        menuclick.add_command(label="Paste",command=self.incolla)
        try:
            menuclick.tk_popup(event.x_root, event.y_root)
        finally:
            menuclick.grab_release()
    def sostituisci(self,*args):
        top= tk.Toplevel(master)
        top.iconbitmap('image/radioactive.ico')
        top.title('Replacer')
        top.geometry("250x150")
        entry1= tk.Entry(top, width= 25)
        entry1.pack()
        entry2= tk.Entry(top, width= 25)
        entry2.pack()
        def doIT():
            testo = self.textarea.get(1.0,tk.END)
            wor = entry1.get()
            wor2 = entry2.get()
            rep = 0
            print(testo)
            testo = testo.replace(wor,wor2)
            self.textarea.delete(1.0,tk.END)
            self.textarea.insert(1.0,testo)
            for word in testo:
                if word==wor:
                    rep+=1
            lab = tk.Label(top,text='Replaced Complete! ').pack(pady=5)
        tk.Button(top,text= "Replace All", command= lambda:doIT()).pack(pady= 5)
        button= tk.Button(top, text="Close", command=lambda:top.destroy())
        button.pack(pady=5)
    def bind_shortcuts(self):
        self.textarea.bind('<Control-n>', self.new_file)
        self.textarea.bind('<Control-o>', self.open_file)
        self.textarea.bind('<Control-s>', self.save_file)
        self.textarea.bind('<Control-S>', self.save_as)
        self.textarea.bind('<Control-h>', self.sostituisci)
        self.textarea.bind('<F5>', self.build)
        self.textarea.bind('<F3>', self.nonASCIIcheck)
        self.textarea.bind('<Alt-F4>', self.chiudi)
        self.textarea.bind('<Key>', lambda event: self.statusbar.update_status(self.textarea.get(1.0,tk.END)))
        self.textarea.bind('<Control-a>', self.selezionaTutto)
        self.textarea.bind('<Control-t>', self.cambiaTema)
        self.textarea.bind('<Control-N>', Menubar.show_new_notes)
        self.textarea.bind('<Control-r>', self.pulisciSchermo)
        self.textarea.bind('<Control-A>', Menubar.show_release_notes)
        self.textarea.bind('<Control-V>', Menubar.show_about_message)
        self.textarea.bind('<Control-o>', self.copia)
        self.textarea.bind('<Control-v>', self.incolla)
        self.textarea.bind('<Control-x>', self.taglia)
        self.textarea.bind('<Control-z>', self.indietro)
        self.textarea.bind('<Control-y>', self.avanti)
        self.textarea.bind('<Control-F>', self.cambiaFont)
        self.textarea.bind('<Control-i>', self.cambiaDimensione)
        self.textarea.bind('<Control-l>', self.cambiaLingua)
        self.textarea.bind('<Control-C>', self.cambiaColore)
        self.textarea.bind('<F2>', self.CheckASCII)
        self.textarea.bind('<Control-d>', self.documents)
        self.textarea.bind('<Control-f>', self.finder)
        self.textarea.bind('<Control-H>', Menubar.helper)
        self.textarea.bind('<Control-T>', self.templates)
        self.textarea.bind('<Control-G>', self.cambiaColoreFG)
        self.textarea.bind('<Button-3>', self.do_popup)
        self.textarea.bind('<Control-j>', self.stampa)
        self.textarea.bind('<Alt-F5>', self.ricarica)
if __name__ =="__main__":
    f = open('wkhtmltopdf/bn.txt','w')
    f.write('0')
    f.close()
    master=tk.Tk()
    master.iconbitmap('image/radioactive.ico')
    pt=PyText(master)
    master.mainloop()
        
