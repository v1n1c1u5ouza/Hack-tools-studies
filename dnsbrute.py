import dns.resolver
import sys


_resolver = dns.resolver.Resolver()
_wordlist = open("/home/kali/myowntools/wordlist.txt", "r")
_subdomains = _wordlist.read().splitlines()

def dns_brute(target):
	print("Iniciando o processo de dnsbrute para o alvo: ", target)
	for subdomain in _subdomains:
		try:
			sub_target = subdomain + "." + target
			result = _resolver.resolve(sub_target, "A")
			for ip in result:
				print(sub_target, "->", ip)
		except:
			pass


if __name__ == "__main__":
	url = sys.argv[1]
	dns_brute(url)


