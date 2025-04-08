<?php

namespace App\Dto;

use Symfony\Component\Validator\Constraints as Assert;

class CategoryDto
{
    public function __construct(
        #[Assert\NotBlank]
        #[Assert\Length(max: 255)]
        public readonly string $name,
    ) {
    }
}