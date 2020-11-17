import http.server
import socketserver
import json

PORT = 8000

dummy_response = {
            "timestamp": 1605007438, 
            "sources":[[40.43871056191201,-3.7108465168370945],[40.438851825209454,-3.6818973265756565],[40.43727428465753,-3.700126460783412],[40.42698788151344,-3.7061092312349646],[40.418527110759335,-3.6824172388098635],[40.437761962690395,-3.683206076649443],[40.436074690982885,-3.7027540001252537],[40.43677273078681,-3.6822265498141418]], 
            "destinations":[[40.41826332937495,-3.711152885700495],[40.41878541533847,-3.7006849874443493],[40.4275920055038,-3.7050225902626486],[40.42075366840505,-3.6873847037798066],[40.4181750475997,-3.688452843710744],[40.437988176503424,-3.6960201188475494],[40.43503311090895,-3.69718215521498],[40.43701483928551,-3.69523147561721]], 
            "data":[[542.3,451.8,236.9,410.3,472.8,126.5,154.3,187.1],[725.5,407.3,395.1,309.8,368.5,226.1,210.3,181.1],[590.6,404,260.2,362.5,425,56.9,93.4,117.5],[374,275.4,24.9,299.9,362.4,227.7,159.8,233.8],[684.3,366.1,353.9,268.6,327.3,184.8,169.1,139.8],[702.3,318.6,428.7,166.1,252.1,424.3,365.6,380.7],[499.5,384,169.1,342.5,405,167.3,99.4,183],[673.8,354.8,343.4,216.5,322.2,255,174.6,190.8]]
        }

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(dummy_response).encode())

with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print(f"Serving at http://127.0.0.1:{PORT}")
    httpd.serve_forever()