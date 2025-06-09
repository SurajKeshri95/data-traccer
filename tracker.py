import psutil
import time

def get_data_usage():
    # Get the current total bytes sent and received since boot
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv

def main():
    print("Tracking data usage... (Press Ctrl+C to stop)\n")
    # Get initial data usage counts
    sent_old, recv_old = get_data_usage()

    try:
        while True:
            time.sleep(1)  # Pause for 1 second
            sent_new, recv_new = get_data_usage()

            # Calculate the differences (bytes per second)
            upload_speed = (sent_new - sent_old) / 1024      # KB/s
            download_speed = (recv_new - recv_old) / 1024      # KB/s
            total_used_mb = (sent_new + recv_new) / (1024 * 1024)  # Convert total to MB

            # Clear the line and print updated stats
            print(f"Upload: {upload_speed:6.2f} KB/s | Download: {download_speed:6.2f} KB/s | Total Used: {total_used_mb:6.2f} MB", end="\r")

            # Update the old values for the next iteration
            sent_old, recv_old = sent_new, recv_new

    except KeyboardInterrupt:
        print("\nStopped tracking.")

if __name__ == "__main__":
    main()
