#/usr/bin/sh

ffmpeg -hide_banner -re -f avfoundation -r 30 -pix_fmt:v yuyv422 -s:v 640x480 -i "0" \
    -c:v h264_videotoolbox -tag:v avc1 -b:v 500k -an -f mpegts "udp://127.0.0.1:5501?pkt_size=1316&buffer_size=65535"
