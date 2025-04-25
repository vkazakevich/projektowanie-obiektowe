package handlers

import (
	"net/http"
	"strings"

	"github.com/labstack/echo/v4"
	"github.com/vkazakevich/projektowanie-obiektowe/Echo/internal/app/models"
	"github.com/vkazakevich/projektowanie-obiektowe/Echo/internal/app/proxy"
	"gorm.io/gorm"
)

func (h *Handler) GetTheWeatherByCity(ctx echo.Context) error {
	city := ctx.Param("city")

	err := syncApiWeatherData(h.DB, ctx.Param("city"))
	if err != nil {
		return ctx.String(http.StatusBadRequest, "bad request")
	}

	var data []models.WeatherData
	h.DB.Where("city LIKE ?", "%"+city+"%").Find(&data)

	return ctx.JSON(http.StatusOK, data)
}

func (h *Handler) GetTheWeatherByCities(ctx echo.Context) error {
	cp := ctx.QueryParam("cities")

	if len(cp) == 0 {
		return ctx.String(http.StatusUnprocessableEntity, "the cities field is required")
	}

	cities := strings.Split(cp, ",")

	for _, c := range cities {
		err := syncApiWeatherData(h.DB, c)

		if err != nil {
			return ctx.String(http.StatusBadRequest, "bad request")
		}
	}

	var data []models.WeatherData
	h.DB.Where("city IN ?", cities).Find(&data)

	return ctx.JSON(http.StatusOK, data)
}

func syncApiWeatherData(DB *gorm.DB, city string) error {
	res, err := proxy.FetchTheWeatherByCity(city)

	if err != nil {
		return err
	}

	apiData := models.WeatherData{City: city, Temperature: res.Temperature, Time: res.Data + " " + res.Time + ":00"}
	DB.Create(&apiData)

	return nil
}
