# livecv (Webcam live streaming with openCV)

## Structure of this application

macOS Ventura 13.4.1

```
    [FaceTime HD Camera] 
      | AVFoundation video device
      |
    [ffmpeg]
      | udp://127.0.0.1:5501 
      |
    [lo0]
      | udp://@:5501 (port forward)
      |
    [docker0]
      | udp://@:5501 (port forward)
      |
* - [eth0] --- Docker container ---------- *
|     | udp://@:5501
|     |
| *-- | --- python app ----------------- *
| | [openCV]
| |   | bytes: image/jpeg
| |   |
| | [Flask]
| |   | http://@:5000/video_feed multipart/x-mixed-replace; boundary=frame
| |   |
| *-- | -------------------------------- *
|     |
* - [eth0] --- Docker container ---------- *
      | http://@:5000/video_feed (port forward)
      |
    [docker0]
      | http://@:5500/video_feed (port forward)
      |
    [lo0]
      | <img src="http://127.0.0.1:5500/video_feed">
      |
    [Browser]

```

## Technical Note

### MJPEG over HTTP

JPEG を multipart/x-mixed-replace により HTTP で返し、動画としてレンダリングさせるものを MJPEG over HTTP と呼ぶことがあります。単に MJPEG や Motion JPEG と呼ぶこともあるようです。

### マルチパート応答

```
Content-Type: multipart/x-mixed-replace: boundary=frame
```

multipart/x-mixed-replace は、 HTTP応答によりサーバーが任意のタイミングで複数の文書を返し、 紙芝居的にレンダリングを切り替えさせるMIMEタイプです。
boundary （区切り文字）は必須パラメータで、指定された文字列の前に “--” を付けてパートを区切ります。

