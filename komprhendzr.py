#data = []
            #for cell in row.split(','):
            #    if cell.strip() != "":
            #        data.append(cell.strip())
            data = [cell.strip() for cell in row.split(',') if cell.strip() != ""]