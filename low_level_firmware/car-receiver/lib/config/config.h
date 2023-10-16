//#define CASA
//#define MOVIL
//#define WEMOS
#define TPLINK

// WIFI EN MOVIL
#ifdef MOVIL
const char* ssid     = "AG4L";
const char* password = "22042204";
const char* hostname = "ESP8266_WeMos";
#endif 
// WIFI ROUTER CASA
#ifdef CASA
const char* ssid     = "vivacable_upglre";
const char* password = "b3uka4wv";
const char* hostname = "ESP8266_WeMos";
#endif
// WIFI EN WEMOS
#ifdef WEMOS
const char* ssid     = "WemosWifi";
const char* password = "WemosPassword";
#endif
// WIFI ROUTER TPLINK
#ifdef TPLINK
const char* ssid     = "TP-Link_DD58";
const char* password = "55118316";
const char* hostname = "acker-car";
#endif

// FIJAR IP, PUERTA Y SUBRED (No usado si useStaticIP = false, como actualmente está)
// Actualmente es la red wifi quien asigna estos valores por defecto
IPAddress ip(192, 168, 0, 137);
IPAddress gateway(192, 168, 0, 1);
IPAddress subnet(255, 255, 255, 0);
