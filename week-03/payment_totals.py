import os

PATH = os.path.join("module-02", "data", "raw_sales.txt")


def clean_amount(text):
    """৳ আর কমা সরিয়ে সংখ্যায় ফেরত দিন।"""
    return float(text.strip().replace("৳", "").replace(",", ""))


def taka(amount):
    """1240.5  →  "৳1240.50" """
    return f"৳{amount:.2f}"


def read_lines(path):
    """ফাইল পড়ে লাইনগুলোর list ফেরত দিন।"""
    with open(path, encoding="utf-8") as fh:
        return fh.read().strip().split("\n")


def main():
    lines = read_lines(PATH)

    bkash_total = 0.0
    bkash_count = 0
    nagad_total = 0.0
    nagad_count = 0
    card_total = 0.0
    card_count = 0
    rocket_total = 0.0
    rocket_count = 0
    cod_total = 0.0
    cod_count = 0

    for raw in lines:
        parts = raw.split(";")
        amount = clean_amount(parts[5])
        payment = parts[6].strip().lower()
        status = parts[7].strip().lower()

        if status == "cancelled":
            continue

        if payment == "bkash":
            bkash_total = bkash_total + amount
            bkash_count = bkash_count + 1
        elif payment == "nagad":
            nagad_total = nagad_total + amount
            nagad_count = nagad_count + 1
        elif payment == "card":
            card_total = card_total + amount
            card_count = card_count + 1
        elif payment == "rocket":
            rocket_total = rocket_total + amount
            rocket_count = rocket_count + 1
        elif payment == "cash on delivery":
            cod_total = cod_total + amount
            cod_count = cod_count + 1

    grand_total = bkash_total + nagad_total + card_total + rocket_total + cod_total

    print("payment ধরে হিসাব (বাতিল বাদে)")
    print()
    print(f"{'bkash':<16}  {bkash_count}টা   {taka(bkash_total)}")
    print(f"{'nagad':<16}  {nagad_count}টা   {taka(nagad_total)}")
    print(f"{'card':<16}  {card_count}টা   {taka(card_total)}")
    print(f"{'rocket':<16}  {rocket_count}টা   {taka(rocket_total)}")
    print(f"{'cash on delivery':<16}  {cod_count}টা   {taka(cod_total)}")
    print()
    print(f"সব মিলিয়ে: {taka(grand_total)}")


if __name__ == "__main__":
    main()
