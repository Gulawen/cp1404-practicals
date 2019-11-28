def main():
    vege = input("Is anyone in your party a vegetarian(Yes/No)")#to gain the data of vege
    vega = input("Is anyone in your party a vegan (Yes/No)")#to gain the data  of vega
    gf = input("Is anyone in your party gluten-free (Yes/No)")#to gain the data of gf
    if vege == "Yes" and vega == "No" and gf == "Yes":#to check the condition if there are yes, no and yes.
        print("Here are your restaurant choices:")
        print("Main Street Pizza, Corner Café and The Chef’s Kitchen")
    elif vege =="No" and vega == "No" and gf == "No":#to check the condition if there are all no
        print("Here are your restaurant choices:")
        print("Joes’ Gourmet Burgers, Main Street Pizza, Corner Cafe, Luigi’s Fine Italian Restaurant and The Chef’s Kitchen ")
    elif vege =="No" and vega =="No" and gf == "Yes":#to check the condition if there are no, no, yes
        print("Here are your restaurant choices:")
        print("Main Street Pizza, Corner Cafe and The Chef’s Kitchen")
    elif vege =="Yes" and vega == "No" and gf == "No":#to check the condition if there are yes, no, no
        print("Here are your restaurant choices:")
        print("Main Street Pizza, Corner Cafe, Luigi’s Fine Italian Restaurant and The Chef’s Kitchen ")
    else:#check if they belong to other condition
        print("Here are your restaurant choices:")
        print("Corner Cafe and The Chef’s Kitchen")
main()
