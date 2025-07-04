package dto

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/vkazakevich/ebiznes/Go/models"
)

func fakeCategoryDto() *CategoryDTO {
	return &CategoryDTO{
		Name: "Test Category",
	}
}

func TestCategoryDto(t *testing.T) {
	dto := fakeCategoryDto()

	assert.NotNil(t, dto)
	assert.NotNil(t, dto.Name)

	assert.Equal(t, "Test Category", dto.Name)
}

func TestCategoryDtoModel(t *testing.T) {
	db := setupTestDB()
	dto := fakeCategoryDto()

	c := models.Category{Name: dto.Name}
	db.Create(&c)

	assert.NotNil(t, c.ID)
	assert.NotNil(t, c.Name)

	assert.Equal(t, c.Name, dto.Name)
}
