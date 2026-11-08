import os

domain = os.getenv("TUNNEL_DOMAIN", "tunnel.example.com")
secret = os.getenv("SECRET_KEY", "BrandNewSecureKey2026#")
resolver = os.getenv("RESOLVER_IP", "1.1.1.1")

config_code = f"""
package com.example.dnstunnel;

public class TunnelConfig {{
    public static final String DOMAIN = "{domain}";
    public static final String SECRET_KEY = "{secret}";
    public static final String RESOLVER_IP = "{resolver}";
}}
"""

os.makedirs("app/src/main/java/com/example/dnstunnel", exist_ok=True)
with open("app/src/main/java/com/example/dnstunnel/TunnelConfig.java", "w") as f:
    f.write(config_code)

print(f"[+] Injected successfully -> Domain: {domain} | Resolver: {resolver}")
