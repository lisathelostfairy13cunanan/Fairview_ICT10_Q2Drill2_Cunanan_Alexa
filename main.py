from pyscript import document, display

# different grade levels from AOT
grade_7 = {"Eren Yeager", "Mikasa Ackerman", "Armin Arlert", "Jean Kirstein"}
grade_8 = {"Sasha Blouse", "Connie Springer", "Historia Reiss"}
grade_9 = {"Reiner Braun", "Bertholdt Hoover", "Annie Leonhart", "Levi Ackerman"}
grade_10 = {"Hange Zoe", "Erwin Smith", "Marco Bott", "Ymir"}

def verify(event):
    first = document.getElementById("firstname").value.strip()
    last = document.getElementById("lastname").value.strip()
    
    new_cadet = {f"{first} {last}".title()}
    all_members = grade_7.union(grade_8, grade_9, grade_10, new_cadet)
    members_list = "<br>".join(sorted(all_members)) 
    2
    total_members = len(all_members)
    
    document.getElementById("result-box").innerHTML = f"""
    <strong>ALL MEMBERS:</strong><br><br>
    {members_list}<br><br>
    <strong>TOTAL MEMBERS:</strong> {total_members}
    """