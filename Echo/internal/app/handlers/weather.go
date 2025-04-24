package handlers

import (
	"net/http"

	"github.com/labstack/echo/v4"
	"github.com/vkazakevich/projektowanie-obiektowe/Echo/internal/app/models"
)

func (h *Handler) GetTheWeatherByCity(ctx echo.Context) error {
	city := ctx.Param("city")

	var data []models.WeatherData
	h.DB.Where("city LIKE ?", "%"+city+"%").Find(&data)

	return ctx.JSON(http.StatusOK, data)
}
