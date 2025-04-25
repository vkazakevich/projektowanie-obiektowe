package utils

import (
	"github.com/vkazakevich/projektowanie-obiektowe/Echo/internal/app/models"
	"gorm.io/gorm"
)

func FillDBSeeds(db *gorm.DB) {
	data := []models.WeatherData{
		{City: "krakow", Temperature: "25", Time: "2025-04-24 12:00"},
		{City: "krakow", Temperature: "10", Time: "2025-04-24 08:00"},
		{City: "krakow", Temperature: "8", Time: "2025-04-24 03:00"},
	}

	db.Create(data)
}
