def oxford_comma(items):
   if len(items) == 1:
        return items[0]
   elif len(items) == 2:
         return f"{items[0]} and {items[1]}"
   else:
        oxford_string = ", ".join(items[:-1])
        oxford_string += f", and {items[-1]}"
        return oxford_string
