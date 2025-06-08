package models

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCategoryModel(t *testing.T) {
	db := setupTestDB()

	t.Run("It creates Category", func(t *testing.T) {
		c := &Category{Name: "Test Category"}
		result := db.Create(&c)

		assert.NoError(t, result.Error)
		assert.Equal(t, int64(1), result.RowsAffected)

		assert.NotNil(t, c.ID)
		assert.Equal(t, "Test Category", c.Name)
	})

	t.Run("It can't creates Category if zero", func(t *testing.T) {
		c := &Category{Name: ""}
		result := db.Create(&c)

		assert.Error(t, result.Error)
		assert.Equal(t, int64(0), result.RowsAffected)

		assert.Equal(t, uint(0), c.ID)

		assert.Equal(t, "", c.Name)
	})
}
