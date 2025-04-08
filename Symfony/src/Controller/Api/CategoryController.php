<?php

namespace App\Controller\Api;

use App\Dto\CategoryDto;
use App\Entity\Category;
use App\Repository\CategoryRepository;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\HttpKernel\Attribute\MapRequestPayload;

#[Route('/api/categories')]
final class CategoryController extends AbstractController
{
    #[Route(name: 'api_category', methods: ['GET'])]
    public function index(CategoryRepository $categoryRepository): JsonResponse
    {
        return $this->json($categoryRepository->findAll());
    }

    #[Route(name: 'api_category_create', methods: ['POST'])]
    public function create(
        #[MapRequestPayload] CategoryDto $categoryDto, 
        CategoryRepository $categoryRepository
    ): JsonResponse
    {
        $category = new Category();
        $category->setName($categoryDto->name);
        $categoryRepository->save($category, true);

        return $this->json($category, Response::HTTP_CREATED);
    }

    #[Route('/{id}', name: 'api_category_show', methods: ['GET'])]
    public function show(Category $category): JsonResponse
    {
        return $this->json($category);
    }

    #[Route('/{id}', name: 'api_category_update', methods: ['PUT'])]
    public function update(
        #[MapRequestPayload] CategoryDto $categoryDto, 
        Category $category,
        CategoryRepository $categoryRepository
    ): JsonResponse
    {
        $category->setName($categoryDto->name);
        $categoryRepository->save($category, true);

        return $this->json($category);
    }

    #[Route('/{id}', name: 'api_category_delete', methods: ['DELETE'])]
    public function delete(Category $category, CategoryRepository $categoryRepository): JsonResponse
    {
        $categoryRepository->remove($category, true);

        return $this->json('', Response::HTTP_NO_CONTENT);
    }
}
