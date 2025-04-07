<?php

namespace App\Dto;

use Symfony\Component\Validator\Constraints as Assert;

class ProductDto
{
    public function __construct(
        #[Assert\NotBlank]
        #[Assert\Length(max: 255)]
        public readonly string $name,

        #[Assert\GreaterThanOrEqual(0)]
        public readonly int $quantity,

        #[Assert\GreaterThanOrEqual(0)]
        public readonly float $price,

        public readonly ?string $description,
    ) {
    }
}