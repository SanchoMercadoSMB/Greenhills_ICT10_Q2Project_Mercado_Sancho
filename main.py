from pyscript import display, document


g7 = {'Chudson Miguelito', 'Sancho Mercado', 'Josua Oritz'}
grade8 = {'Brent Fuente', 'Sonion Soupleton', 'Monkey Luffy'}
g9 = {'Maria Santos', 'Julius Ceaser', 'Sebastian Cruz'}
grade10 = {'Dejucos Villantos', 'Bob Dillingham', 'Ousmane Dembele', 'Nick Gurds'}
members = g7 | grade8 | g9 | grade10

def student_club(e):
    document.getElementById("club_output").innerHTML = ''
    
    lastname = document.getElementById("club_last_name").value.strip()
    firstname = document.getElementById("club_first_name").value.strip()
    
    ICT_list = [('darren', 'watkins'), ('rob', 'dillingham'), ('joshua', 'ortiz'), ('kristine', 'pasco')]
    chk = (firstname.lower(), lastname.lower()) in ICT_list

    msgs = [
        f'Sorry {firstname} {lastname}, your name is not on the list.',
        f'Congratulations, {firstname} {lastname}! You are now part of the ICT club. SO TUFF!!'
    ]

    display(msgs[chk], target="club_output")

def add_member(event):
    f_name = document.getElementById("first_name").value.strip()
    l_name = document.getElementById("last_name").value.strip()
    out = document.getElementById("output")

    if f_name == "" or l_name == "":
        out.innerHTML = "Please type both a first and last name."
        return

    members.add(f_name + " " + l_name)
    out.innerHTML = f"{sorted(members)} <br><br> Total Members: {len(members)}"

document.getElementById("status").innerHTML = "python is ready!"