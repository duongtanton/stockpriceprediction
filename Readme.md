# Bài tập cá nhân phần ứng dụng Machine Learning

## Giới thiệu
Thông tin sinh viên - MSSV: 20120598 - Họ Và Tên: Dương Tấn Tồn 

Trong bài tập này, sẽ thực hiện theo tutorial để làm quen với mô hình dự đoán và triển khai ứng dụng trên môi trường web. Cụ thể, sẽ dự đoán giá của các cặp tiền sau: BTC-USD, ETH-USD, ADA-USD. 

Mục tiêu của bài tập là giúp nắm bắt được quy trình xây dựng và triển khai một mô hình Machine Learning từ giai đoạn tiền xử lý dữ liệu, xây dựng mô hình, đến việc triển khai mô hình lên môi trường web và quay lại video demo sản phẩm.

## Hướng dẫn thực hiện

### 1. Chuẩn bị dữ liệu

- **Nguồn dữ liệu**: Sử dụng yfinance để thu thập dữ liệu lịch sử giá của các cặp tiền BTC-USD, ETH-USD, ADA-USD.
- **Tiền xử lý dữ liệu**: Làm sạch và chuẩn hóa dữ liệu để phù hợp với yêu cầu của mô hình Machine Learning. Các bước tiền xử lý có thể bao gồm:
  - Loại bỏ dữ liệu thiếu
  - Tính các chỉ số kỹ thuật (moving averages, RSI, MACD, etc.)
  - Chia dữ liệu thành tập huấn luyện và tập kiểm tra

### 2. Xây dựng mô hình Machine Learning

- **Lựa chọn mô hình**: Mô hình dự đoán như LSTM.
- **Huấn luyện mô hình**: Sử dụng tập huấn luyện để huấn luyện mô hình và tối ưu hóa các tham số.
- **Đánh giá mô hình**: Sử dụng tập kiểm tra để đánh giá hiệu quả của mô hình bằng các chỉ số như RMSE, MAE, hay MAPE.

### 3. Triển khai mô hình trên môi trường web

- **Xây dựng API**: Sử dụng dash
- **Giao diện người dùng**: Sử dụng dash để xây dựng giao diện người dùng cho ứng dụng web. Giao diện này sẽ cho phép người dùng nhập dữ liệu và hiển thị kết quả dự đoán.

### 4. Quay lại video demo sản phẩm

- **Nội dung video**: Video demo nên bao gồm các phần sau:
  - Giới thiệu về ứng dụng và chức năng chính.
  - Hướng dẫn cách sử dụng ứng dụng.
  - Ví dụ cụ thể về việc dự đoán giá của các cặp tiền BTC-USD, ETH-USD, ADA-USD.
- **Video demo**: [tại đây](https://youtu.be/LmpA8PTFl8Y)

## Kết thúc
