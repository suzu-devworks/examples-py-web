#/usr/bin/sh

# ffmpeg -hide_banner -re -f avfoundation -r 30 -pix_fmt:v yuyv422 -s:v 1280x720 -i "0:1" \
#     -c:v hevc_videotoolbox -tag:v hvc1 -b:v 5000k \
#     -flags +cgop -g 30 -filter:v yadif \
#     -acodec aac -ab 128k -ac 2 \
#     -threads 1 \
#     -f hls \
#     -hls_time 4 \
#     -hls_allow_cache 0 \
#     -hls_flags delete_segments \
#     -hls_segment_type fmp4 \
#     -hls_fmp4_init_filename init.mp4 \
#     -hls_segment_filename 'live-%03d.m4s' \
#     playlist.m3u8

ffmpeg -hide_banner -re -f avfoundation -r 30 -pix_fmt:v yuyv422 -s:v 1280x720 -i "0:1" \
    -c:v h264_videotoolbox -tag:v aac1 -b:v 5000k \
    -flags +cgop -g 30 -filter:v yadif \
    -acodec aac -ab 128k -ac 2 \
    -threads 1 \
    -f hls \
    -hls_time 4 \
    -hls_allow_cache 0 \
    -hls_flags delete_segments \
    -hls_segment_type mpegts \
    -hls_segment_filename 'live-%03d.ts' \
    playlist.m3u8

# https://hlsjs.video-dev.org/demo/
# http://localhost:5000/livestreaming/video/playlist.m3u8

