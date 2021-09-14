# genome = input("Enter a Genome string: ")
genome = "TTATGTTTTAAGGATGGGGCGTTAGTT"

lenght = len(genome)
count_1 = 0
count_2 = 0
failsafe = 0
end_of_genome = 0
beginning_of_genome = 0


while "ATG" in genome[end_of_genome:lenght]:
    failsafe += 1
    while True:
        if genome[count_1] == "A" and genome[count_1 + 1] == "T" and genome[count_1 + 2] == "G":
            beginning_of_genome = count_1 + 3
            count_2 = beginning_of_genome
            break
        else:
            count_1 += 1

    if (
        "TAG" in genome[beginning_of_genome:lenght]
        or "TGA" in genome[beginning_of_genome:lenght]
        or "TAA" in genome[beginning_of_genome:lenght]
    ):
        while True:
            if (
                genome[count_2] == "T"
                and genome[count_2 + 1] == "A"
                and genome[count_2 + 2] == "G"
                or genome[count_2] == "T"
                and genome[count_2 + 1] == "G"
                and genome[count_2 + 2] == "A"
                or genome[count_2] == "T"
                and genome[count_2 + 1] == "A"
                and genome[count_2 + 2] == "A"
            ):
                end_of_genome = count_2
                print(genome[beginning_of_genome:end_of_genome])
                beginning_of_genome = end_of_genome + 1
                count_1 = end_of_genome
                break
            else:
                count_2 += 1

    else:
        print(genome[beginning_of_genome:lenght])
        end_of_genome = lenght

else:
    if failsafe < 1:
        print("no gene is found.")
