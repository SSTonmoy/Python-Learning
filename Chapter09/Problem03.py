# Write a program to generate multiplication tables from 2 to 20 and write it to the different files.
# Place these files in a folder for a 13-year-old.
def multiplication_tables():
    for i in range(2, 21):
        with open(f'13_Year_Old_Boy/multiplication_table_of_{i}.txt', 'w') as f:
            f.write(f'This is the multiplication table of {i}\n\n')
            for j in range(1, 11):
                f.write(f'{i} X {j} = {i * j}\n')


multiplication_tables()
