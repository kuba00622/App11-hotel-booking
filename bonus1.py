
import pandas
from fpdf import FPDF
from fpdf.enums import XPos, YPos

df = pandas.read_csv("articles.csv", dtype={'id': str})

class Article:
    def __init__(self, article_id):
        self.article_id = article_id
        self.name = df.loc[df['id'] == self.article_id, 'name'].squeeze()
        self.price = df.loc[df['id'] == self.article_id, 'price'].squeeze()

class Receipt:
    def __init__(self, Article_number, Article_object):
        self.Article_number = Article_number
        self.Article_object = Article_object

    def get_receipt(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, text=(f"Receipt number: {self.Article_object.article_id}"),
                 new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.cell(w=50, h=8, text=(f"Article: {self.Article_object.name}"),
                 new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.cell(w=50, h=8, text=(f"Price: {self.Article_object.price}"),
                 new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.output(f"receipt.pdf")

print(df)
article_ID = input("Choose an article to buy: ")
produkt = Article(article_ID)
paragon = Receipt(Article_number=article_ID, Article_object=produkt)
paragon.get_receipt()

