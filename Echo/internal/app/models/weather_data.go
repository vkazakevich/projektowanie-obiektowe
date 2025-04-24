package models

type WeatherData struct {
	ID          uint   `gorm:"primarykey"`
	City        string `json:"city"`
	Temperature string `json:"temperature"`
	Time        string
}
