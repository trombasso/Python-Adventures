from random import uniform


def estimate_PI(hits):
    totalhits = 0
    for i in range(0, hits):
        if uniform(-1.00, 1.00) ** 2 + uniform(-1.00, 1.00) ** 2 - 1 ** 2 < 0:
            totalhits += 1
    print(f"PI estimates to {(4 * totalhits) / hits } based on {totalhits} points of calculation.")


if __name__ == "__main__":
    estimate_PI(int(input("How many reference points? ")))
