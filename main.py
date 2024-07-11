import gpt_response as gpt
import document as doc


def main():
    doc1 = doc.Document(1, gpt.d1)
    print(doc1.tokens)


if __name__ == "__main__":
    main()

