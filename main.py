lines=int(input("How many lines of 𝜋-thon do you want?: "))

stringx=""
#Empty strings to append the python equivalents and print the full python line of code

for line in range(0,lines):

  code=input("\nEnter a line of code: ")
  list=[*code] #Splits the input into a list of its individual characters
  
  for character in list:
    if character=="π":
      stringx+="print"
    elif character=="θ":
      stringx+="#"
    elif character=="Σ":
      stringx+="str"
    elif character=="ι":
      stringx+="int"
    elif character=="ο":
      stringx+="float"
    elif character=="ρ":
      stringx+="range"
    elif character=="τ":
      stringx+="True"
    elif character=="Δ":
      stringx+="False"
    elif character=="Ξ":
      stringx+="="
    elif character=="ν":
      stringx+="\n"
    elif character=="Ψ":
      stringx+="\f"
    elif character=="η":
      stringx+="\t"
    elif character=="β":
      stringx+="\b"
    elif character=="μ":
      stringx+="+"
    elif character=="δ":
      stringx+="-"
    elif character=="χ":
      stringx+="*"
    elif character=="Ω":
      stringx+="/"
    elif character=="Θ":
      stringx+="%"
    elif character=="γ":
      stringx+=">"
    elif character=="λ":
      stringx+="<"
    elif character=="Ι":
      stringx+="  "
    elif character=="υ":
      stringx+="if"
    elif character=="κ":
      stringx+="elif"
    elif character=="Λ":
      stringx+="else"
    elif character=="α":
      stringx+="and"
    elif character=="Ο":
      stringx+="or"
    elif character=="Ν":
      stringx+="!"
    elif character=="ω":
      stringx+="while"
    elif character=="Γ":
      stringx+="for"
    elif character=="φ":
      stringx+="break"
    elif character=="ς":
      stringx+="continue"
    elif character=="ε":
      stringx+="input"
    
    else:
      stringx+=character #Prints a character as-is if it isn't a Greek letter

exec(stringx)
  