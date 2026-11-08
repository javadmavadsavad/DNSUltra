import os

# مقادیری که شما می‌دهید
DOMAIN = os.getenv("TUNNEL_DOMAIN", "your-domain.com")
SECRET_KEY = os.getenv("SECRET_KEY", "BrandNewSecureKey2026#")
RESOLVER_IP = os.getenv("RESOLVER_IP", "1.1.1.1")

config_code = f"""
package com.example.dnstunnel;

public class TunnelConfig {{
    public static final String DOMAIN = "{DOMAIN}";
    public static final String SECRET_KEY = "{SECRET_KEY}";
    public static final String RESOLVER_IP = "{RESOLVER_IP}";
}}
"""

os.makedirs("app/src/main/java/com/example/dnstunnel", exist_ok=True)
with open("app/src/main/java/com/example/dnstunnel/TunnelConfig.java", "w") as f:
    f.write(config_code)

print("[+] Config injected successfully!")
