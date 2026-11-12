import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/users/1")
print(response.status_code)
print(response.json())

print("-----")

response = httpx.get("https://jsonplaceholder.typicode.com/users")
utilisateurs = response.json()
for chaque_utilisateurs in utilisateurs:
    print(f"{chaque_utilisateurs['name']} | {chaque_utilisateurs['email']}")

print(len(utilisateurs))