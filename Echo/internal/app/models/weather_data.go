package models

type WeatherData struct {
	ID          uint   `gorm:"primarykey"`
	City        string `json:"city" gorm:"uniqueIndex:idx_city_time"`
	Temperature string `json:"temperature"`
	Time        string `json:"time" gorm:"uniqueIndex:idx_city_time"`
}
