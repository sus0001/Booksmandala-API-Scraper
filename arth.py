def arithmetic_arranger(problems, bool=False):
    if bool:
        new_one = []
        arrange_problems = []
        if len(problems) > 5:
            return "Error: Too many problems."
        else:
            pass    
        operators = ['+', '-']
        splits = [problem.split() for problem in problems]
        
        for probs in splits:
            if not probs[0].isdigit() or not probs[-1].isdigit():
                return "Error: Numbers must only contain digits."
            elif len(probs[0]) > 4 or len(probs[-1]) > 4:
                return "Error: Number cannot be more than four digits."
            elif not probs[1] in operators:
                return "Error: Operator must be '+' or '-'."
            
            elif len(probs[0]) < len(probs[-1]) or len(probs[0]) == len(probs[-1]):
                  # Caluclating the total number of dots. The logic calculates the the total number of greatest number of each iteration with added +2 and voila there's perfect dots:
                  dotted_char = f"{(len(probs[-1])+2)*'-'}"
                  # Calculating the upper the space for addend:
                  upper_one = (len(dotted_char) - len(probs[0])) * " "
                  # Final arithmetic arranger:
                  final_one = (f"{upper_one}{probs[0]}\n{probs[1]} {probs[-1]}\n{dotted_char}")        
                  arrange_problems.append(final_one)                     
            else:
                # Caluclating the total number of dots. The logic calculates the the total number of greatest number of each iteration with added +2 and voila there's perfect dots:
                dotted_char = f"{(len(probs[0])+2)*'-'}"
                # Calculating the upper the space for addend:
                lower_one = (len(dotted_char)-1 - len(probs[-1])) * " "
                # Final arithmetic arranger:
                final_one = f"  {probs[0]}\n{probs[1]}{lower_one}{probs[-1]}\n{dotted_char}"
                ## print(final_one)        
                arrange_problems.append(final_one)
        
        return arrange_problems
