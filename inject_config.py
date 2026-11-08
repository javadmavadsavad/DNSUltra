import os

domain = os.getenv("TUNNEL_DOMAIN", "tunnel.example.com")
secret = os.getenv("SECRET_KEY", "BrandNewSecureKey2026#")
resolver = os.getenv("RESOLVER_IP", "1.1.1.1")

# ۱. ایجاد پوشه‌ها
os.makedirs("app/src/main/java/com/example/dnstunnel", exist_ok=True)

# ۲. تزریق تنظیمات
with open("app/src/main/java/com/example/dnstunnel/TunnelConfig.java", "w") as f:
    f.write(f"""package com.example.dnstunnel;
public class TunnelConfig {{
    public static final String DOMAIN = "{domain}";
    public static final String SECRET_KEY = "{secret}";
    public static final String RESOLVER_IP = "{resolver}";
}}
""")

# ۳. مانیفست اندروید
with open("app/src/main/AndroidManifest.xml", "w") as f:
    f.write("""<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.dnstunnel">
    <uses-permission android:name="android.permission.INTERNET" />
    <application
        android:allowBackup="true"
        android:label="DNS Tunnel"
        android:theme="@android:style/Theme.NoTitleBar">
        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
""")

# ۴. تنظیمات build.gradle ریشه
with open("build.gradle", "w") as f:
    f.write("""buildscript {
    repositories {
        google()
        mavenCentral()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:8.1.1'
    }
}
allprojects {
    repositories {
        google()
        mavenCentral()
    }
}
""")

with open("settings.gradle", "w") as f:
    f.write("include ':app'\n")

# ۵. تنظیمات build.gradle ماژول app
with open("app/build.gradle", "w") as f:
    f.write("""apply plugin: 'com.android.application'

android {
    namespace 'com.example.dnstunnel'
    compileSdkVersion 33
    defaultConfig {
        applicationId "com.example.dnstunnel"
        minSdkVersion 21
        targetSdkVersion 33
        versionCode 1
        versionName "1.0"
    }
}
dependencies {
    implementation 'androidx.appcompat:appcompat:1.6.1'
}
""")

# ۶. کد اصلی برنامه
with open("app/src/main/java/com/example/dnstunnel/MainActivity.java", "w") as f:
    f.write("""package com.example.dnstunnel;
import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        TextView tv = new TextView(this);
        tv.setText("DNS Tunnel Active\\nDomain: " + TunnelConfig.DOMAIN);
        setContentView(tv);
    }
}
""")

print("✅ Complete Android Project Generated!")
