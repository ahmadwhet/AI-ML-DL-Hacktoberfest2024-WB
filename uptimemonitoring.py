def monitor_uptime_with_alerts(url, check_interval):
    print(f"Starting uptime monitor for {url}")
    was_down = False
    while True:
        status = check_website_status(url)
        if status:
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {url} is UP")
            if was_down:
                send_email_alert(f"Website {url} is UP", f"The website {url} is back online.")
                was_down = False
        else:
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {url} is DOWN")
            if not was_down:
                send_email_alert(f"Website {url} is DOWN", f"The website {url} appears to be down.")
                was_down = True
        time.sleep(check_interval)

# Monitor a website and send alerts if the status changes
monitor_uptime_with_alerts("https://example.com", 60)
