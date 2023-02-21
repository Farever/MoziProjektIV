from fpdf import FPDF
import qrcode
import database as db
from classes import reservation
from classes import movie

class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Calculating width of title and setting cursor position:
        width = self.get_string_width(self.title) + 6
        self.image("logo-color.png" ,10, 8, 33)
        self.set_x((210 - width) / 2)
        self.set_text_color(0, 51, 102)
        # Setting thickness of the frame (1 mm)
        self.set_line_width(1)
        # Printing title:
        self.cell(
            width,
            9,
            self.title,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
        )
        # Performing a line break:
        self.ln(30)

    def footer(self):
        # Setting position at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Setting text color to gray:
        self.set_text_color(128)
        # Printing page number
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def chapter_title(self, num):
        # Setting font: helvetica 12
        self.set_font("helvetica", "", 12)
        # Setting background color
        self.set_fill_color(200, 220, 255)
        # Printing chapter name:
        self.cell(
            0,
            6,
            f"Foglalási szám: {num}",
            new_x="LMARGIN",
            new_y="NEXT",
            align="L",
            fill=True,
        )
        # Performing a line break:
        self.ln(4)

    def chapter_body(self, orderID):
        global Reservations
        global chairlist
        # Reading text file:
        Reservations = db.selectReservation(orderID)
        name = Reservations[0].lastName + " " + Reservations[0].firstName
        chairlist = []
        for Reservation in Reservations:
            chairlist.append(Reservation.chair)
        
        # Setting font: Times 12
        self.set_font("Times", size=12)
        # Printing justified text:
        self.cell(0,5, "Név: " + name)
        self.ln()
        self.cell(0,5, "Terem: " + str(Reservations[0].hall))
        self.ln()
        self.cell(0,5, "Székek: " + ' '.join(map(str, chairlist)))
        self.ln()
        # Final mention in italics:
        self.set_font(style="I")

    def print_chapter(self, orderID):
        self.add_page()
        self.chapter_title(orderID)
        self.chapter_body(orderID)

    def generateCode(self):
    #Creating a QRCode object of the size specified by the user
        qr = qrcode.QRCode(version = 1,
                box_size = 10,
                border = 5)
        qr.add_data("Terem: " + str(Reservations[0].hall) + " " + "Székek: " + ' '.join(map(str, chairlist)))
        qr.make(fit = True) #Making the entire QR Code space utilized
        img = qr.make_image() #Generating the QR Code
        img.save('qr.png') #Saving the QR Code
        self.image("qr.png")

pdf = PDF()
pdf.set_title("MoziTown jegyfoglalás")
pdf.print_chapter(1)
pdf.generateCode()
pdf.output("tuto3.pdf")