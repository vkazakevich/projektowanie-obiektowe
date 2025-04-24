package handlers

import (
	"net/http"

	"github.com/labstack/echo/v4"
	"github.com/vkazakevich/projektowanie-obiektowe/Echo/internal/app/models"
	"github.com/vkazakevich/projektowanie-obiektowe/Echo/internal/app/proxy"
)

func (h *Handler) GetTheWeatherByCity(ctx echo.Context) error {
	city := ctx.Param("city")

	var data []models.WeatherData
	h.DB.Where("city LIKE ?", "%"+city+"%").Find(&data)

	res, err := proxy.FetchTheWeatherByCity(city)

	if err != nil {
		return ctx.String(http.StatusBadRequest, "bad request")
	}

	apiData := &models.WeatherData{City: city, Temperature: res.Temperature, Time: res.Data + " " + res.Time + ":00"}

	return ctx.JSON(http.StatusOK, apiData)
}
