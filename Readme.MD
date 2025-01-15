# Bài Test DevOps

## Yêu cầu hệ thống (Requirements)

Hệ thống cần cài đặt trước khi triển khai:

- **Docker**
- **Docker Compose**
- Hệ điều hành: Linux hoặc macOS

---

## Giới thiệu các thành phần hệ thống

Hệ thống bao gồm nhiều thành phần để giám sát và cảnh báo:

### **1. Python App**
- Ứng dụng API demo viết bằng Python.
- Gồm 2 route:
  - `/test-devops`: Luôn trả HTTP 200.
  - `/simulate-error`: Trả HTTP 502 nếu MongoDB không kết nối được.

### **2. Prometheus**
- Thu thập dữ liệu giám sát từ các exporter.

### **3. Alertmanager**
- Gửi cảnh báo khi API gặp lỗi HTTP 502 hoặc không truy cập được.
- Cảnh báo gửi tới Slack channel.

### **4. Node Exporter**
- Giám sát tài nguyên hệ thống: CPU, RAM, Disk...

### **5. Blackbox Exporter**
- Kiểm tra trạng thái và mã HTTP từ API (success rate, latency).

### **6. MongoDB**
- Cơ sở dữ liệu dùng để kiểm tra kết nối từ Python App.

### **6. Request Generator**
- Tự động gửi request đến API /test-devops khi hệ thống khởi động.
- Giúp giả lập lưu lượng request thực tế cho API.

---

## Hướng dẫn sử dụng

### **1. Clone repository**

```bash
git clone https://github.com/tquocthang97/baitest-devops.git
cd baitest-devops
```

### **2. Chạy Docker Compose**

```bash
docker-compose up -d
```
---

## Giám sát trên Grafana

Truy cập Grafana tại [http://localhost:3000](http://localhost:3000):

- **Tài khoản:** `admin`
- **Mật khẩu:** `admin`

### **1. Dashboard giám sát:**
- **Server:** CPU, RAM, Disk.
- **Blackbox Exporter:** Trạng thái và thời gian phản hồi API.
- **Tổng quan:** API success rate, resource usage, performance, latency.

---

## Kiểm tra cảnh báo

### **1. Ngắt MongoDB để kiểm tra:**

```bash
docker-compose stop mongo
```

- API `test-devops` sẽ trả HTTP 502 do không kết nối được đến MongoDB.
- Kiểm tra Slack channel nhận cảnh báo: [Slack Channel](https://join.slack.com/t/test-devops-org/shared_invite/zt-2xq38lhrr-9q0IW5kvZvXThoSLhchZFg).

### **2. Bật lại MongoDB:**

```bash
docker-compose start mongo
```

---

