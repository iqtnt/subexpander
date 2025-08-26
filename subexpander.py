import argparse

def extract_domains(domain, start_level):
    parts = domain.strip().split(".")
    results = []
    
    for i in range(len(parts) - 2):
        sub = ".".join(parts[i:])
        results.append(sub)

    results.append(".".join(parts[-2:]))

    results = sorted(results, key=lambda x: x.count("."))

    return results[start_level - 1:]


def main():
    parser = argparse.ArgumentParser(description="SubExpander - Expand domains to subdomain levels")
    parser.add_argument("-list", required=True, help="File with list of domains")
    parser.add_argument("-o", "--output", default="subexpander.txt", help="Output file for results")
    parser.add_argument(
    "-l", "--level",
    type=int,
    choices=[1, 2, 3],
    default=1,
    help="-l Subdomain level to extract: 1.com | 2.evil.com | 3.ev.evil.com"
)

    args = parser.parse_args()

    with open(args.list, "r") as f:
        original_domains = [line.strip() for line in f if line.strip()]

    original_count = len(original_domains)
    all_results = set()

    for domain in original_domains:
        expanded = extract_domains(domain, args.level)
        all_results.update(expanded)

    new_count = len(all_results)

    with open(args.output, "w") as f:
        for d in sorted(all_results):
            f.write(d + "\n")

    print(f"[+] Original domains: {original_count}")
    print(f"[+] Expanded domains: {new_count}")
    print(f"[+] Results saved in {args.output}")


if __name__ == "__main__":
    main()
