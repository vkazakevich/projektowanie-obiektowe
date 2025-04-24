package handlers

import (
	"net/http"

	"github.com/labstack/echo/v4"
)

type WeatherData struct {
	Temperature string
	Time        string
}

func (h *Handler) GetTheWeatherByCity(ctx echo.Context) error {
	if ctx.Param("city") != "krakow" {
		return ctx.String(http.StatusNotFound, "weather data not found")
	}

	var list []WeatherData

	list = append(list, WeatherData{Temperature: "25", Time: "12:00"})
	list = append(list, WeatherData{Temperature: "10", Time: "8:00"})
	list = append(list, WeatherData{Temperature: "8", Time: "03:00"})

	return ctx.JSON(http.StatusOK, list)
}
